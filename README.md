# rosidl-to-fastdds

## ビルド

```bash
docker build -t rosidl-to-fastdds --build-arg ROS_DISTRO=humble --build-arg FASTDDSGEN_VERSION=v3.3.0 .
```

## 使い方

ROS2ワークスペースやらに移動してから以下のコマンドを実行する(変換している.msgはあくまで例)

```bash
docker run --rm -v $(pwd):/workdir rosidl-to-fastdds --outdir /workdir/out \
  src/rcl_interfaces/builtin_interfaces/msg/Time.msg \
  src/common_interfaces/std_msgs/msg/Header.msg \
  src/common_interfaces/sensor_msgs/msg/Joy.msg
```
