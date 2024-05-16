from nonebot.plugin import PluginMetadata

from .consts import FEISHU as FEISHU
from .consts import ONEBOT as ONEBOT
from .consts import QQGUILD as QQGUILD
from .consts import TELEGRAM as TELEGRAM
from .deps import EventName as EventName
from .deps import AdapterName as AdapterName
from .rule import allow_adapters as allow_adapters
from .permission import PRIVATEMESSAGE as PRIVATEMESSAGE
from .deps import ImageSegmentMethod as ImageSegmentMethod
from .rule import is_private_message as is_private_message
from .deps import MessageSegmentClass as MessageSegmentClass

__plugin_meta__ = PluginMetadata(
    name="plugin-params",
    description="提供便利的函数用于实现多适配器兼容",
    usage="from nonebot_plugin_params import is_private_message",
    homepage="https://github.com/iyume/nonebot-plugin-params",
    type="library",
    config=None,
    supported_adapters={"~onebot.v11", "~qq", "~feishu", "~telegram"},
    extra={
        "author": "iyume",
        "priority": 1,
        "version": "0.1.1",
    },
)
