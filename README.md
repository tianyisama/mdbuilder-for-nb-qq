# 如何使用
在确保了你已经安装了`qq-adapter`的情况下，将`markdown.py`及`keyboard.py`放到插件目录下即可，使用前记得在`markdown.py`里填入你的md模板id
## 构造方法示例
### markdown
> 参数请填入你申请的模板里的参数
```python
from .markdown import MarkdownBuilder

test_value = "这是一个变量的值"

params = {
    'text_start': test_value,  # 直接使用变量
    'img_url': 'https://qqminiapp.cdn-go.cn/open-platform/11d80dc9/img/robot.b167c62c.png',
    'img_dec': '图片 #240px #240px'
}

markdown_message = MarkdownBuilder.markdown(params)
```

### keyboard
> 构造按钮的参数具体参考 [Keyboard 构造方式](https://bot.q.qq.com/wiki/develop/api-v2/server-inter/message/trans/msg-btn.html)
```python
from .keyboard import KeyboardBuilder

button1 = KeyboardBuilder.button(
    id="1",
    label="Ciallo～(∠・ω<)",
    visited_label="咕噜噜",
    style=1,
    action_type=2,
    permission_type=2,
    action_data="Ciallo～(∠・ω<)",
    enter=True,
    unsupport_tips="客户端不支持时的提示"
)
button2 = KeyboardBuilder.button(
    id="2",
    label="114514",
    visited_label="哼哼啊啊啊啊啊啊",
    style=0,
    action_type=2,
    permission_type=2,
    action_data="114514"
)
keyboard = KeyboardBuilder.keyboard([button1, button2])

```
### 完整的实现示例
```python
from .markdown import MarkdownBuilder
from .keyboard import KeyboardBuilder

nana= on_command('test', aliases={'123'}, priority=10, block=True)

button1 = KeyboardBuilder.button(
    id="1",
    label="再来一次",
    visited_label="阿巴阿巴",
    style=1,
    action_type=2,
    permission_type=2,
    action_data="/456",
    enter=True,
    unsupport_tips="客户端不支持时的提示"
)
button2 = KeyboardBuilder.button(
    id="2",
    label="拾雪昨晚很激烈",
    visited_label="咕噜噜",
    style=0,
    action_type=2,
    permission_type=2,
    action_data="data2"
)
keyboard = KeyboardBuilder.keyboard([button1, button2])
@nana.handle()
async def _():
    text = "this is a test"
    try:
        params = {
            'text_start': text,
            'img_url': 'https://qqminiapp.cdn-go.cn/open-platform/11d80dc9/img/robot.b167c62c.png',
            'img_dec': '图片 #240px #480px'
        }
        markdown_message = MarkdownBuilder.markdown(params)
        combined_message = markdown_message + keyboard
        await nana.send(combined_message)
    except Exception as e:
        await nana.send(f"{e}")

```
