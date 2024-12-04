#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/3 15:19
# @Author  : Heshouyi
# @File    : urls.py
# @Software: PyCharm
# @description:

from django.urls import path
from .views import (
    connect, disconnect, start_heartbeat, stop_heartbeat,
    send_custom_command, alarm_report, alarm_recovery_report,
    car_trigger_event, car_back_event, car_traffic_event
)
