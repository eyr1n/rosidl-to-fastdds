# rosidl-to-fastdds

## 使い方

ROS2ワークスペースやらに移動してから以下のコマンドを実行する(変換している.msgはあくまで例)

```bash
docker run --rm -v $(pwd):/workdir eyr1n/rosidl-to-fastdds:3.3.0-humble --outdir /workdir/out \
  src/rcl_interfaces/builtin_interfaces/msg/Time.msg \
  src/common_interfaces/std_msgs/msg/Header.msg \
  src/common_interfaces/sensor_msgs/msg/Joy.msg
```

## ビルド(自分用)

```bash
docker build --platform linux/amd64,linux/arm64 \
  -t eyr1n/rosidl-to-fastdds:3.3.0-humble \
  --build-arg ROS_DISTRO=humble \
  --build-arg FASTDDSGEN_VERSION=v3.3.0 .
```
