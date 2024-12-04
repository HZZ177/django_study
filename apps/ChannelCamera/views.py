from django.shortcuts import render

# Create your views here.

@require_http_methods
def connect():
    """
    尝试连接设备到服务器
    连接后发送注册包并开启心跳
    :return:
    """
    logger.info("通道相机connect接口被调用")
    camera = get_channel_camera()
    camera.connect()
    logger.info("通道相机成功连接服务器")
    return success_response()