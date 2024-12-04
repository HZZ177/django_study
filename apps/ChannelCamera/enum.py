#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/3 11:39
# @Author  : Heshouyi
# @File    : enum.py
# @Software: PyCharm
# @description:

from enum import Enum


class CarTriggerFlag(Enum):
    """
    相机触发事件枚举值
    2-去车
    3-来车
    """
    TO_CAR = 2
    FROM_CAR = 3


class CarBackFlag(Enum):
    """
    相机后退事件枚举值
    9-来车后车辆又后退
    9-去车后车辆又后退
    """
    BACK_FROM_CAR = 9
    BACK_TO_CAR = 10


class CarColour(Enum):
    """
    车牌颜色枚举值
    0：无  1："白",  2："黑", 3："蓝", 4："黄", 5："绿"，6："红"
    """
    NONE = 0
    WHITE = 1
    BLACK = 2
    BLUE = 3
    YELLOW = 4
    GREEN = 5
    RED = 6


class AreaState(Enum):
    """
    区域交通流量状态枚举值
    0：正常；1：繁忙；2：拥堵
    """
    NORMAL = 0
    BUSY = 1
    JAM = 2


class CameraFaultType(Enum):
    """
    相机故障类型枚举值
    videoFault：视频故障
    algNotWork：算法未正常运行
    jpgEncodeFault：图片编码失败
    ossNetFault：连接图片服务器oss失败
    NetFault：网络故障
    """
    VIDEO_FAULT = "videoFault"
    ALG_NOT_WORK = "algNotWork"
    JPG_ENCODE_FAULT = "jpgEncodeFault"
    OSS_NET_FAULT = "ossNetFault"
    NET_FAULT = "NetFault"
