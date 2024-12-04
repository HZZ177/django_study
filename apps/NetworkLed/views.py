from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from utils.logger import logger
from ..DeviceManager import device_manager


@require_http_methods(["POST"])
def disconnect():
    """
    断开服务器连接
    :return:
    """
    logger.info("LED网络屏disconnect接口被调用")
    network_led = get_network_led()
    network_led.disconnect()
    logger.info("LED网络屏成功断开连接")
    return success_response()