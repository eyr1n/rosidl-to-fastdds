FROM ubuntu:22.04

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y \
    git cpp openjdk-17-jdk python3 python3-empy python3-catkin-pkg

WORKDIR /rosidl-to-fastdds

COPY rosidl_to_fastdds.py .

# rosidl_adapter
ARG ROS_DISTRO=humble
RUN git clone -b $ROS_DISTRO https://github.com/ros2/rosidl.git && \
    cp -R rosidl/rosidl_adapter/rosidl_adapter .

# Fast-DDS-Gen
ARG FASTDDSGEN_VERSION=v3.3.0
RUN git clone -b $FASTDDSGEN_VERSION --recursive https://github.com/eProsima/Fast-DDS-Gen.git && \
    cd Fast-DDS-Gen && \
    ./gradlew assemble

WORKDIR /workdir

ENTRYPOINT ["python3", "/rosidl-to-fastdds/rosidl_to_fastdds.py"]
