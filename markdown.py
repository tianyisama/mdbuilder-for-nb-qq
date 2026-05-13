from nonebot.adapters.qq import MessageSegment
from nonebot.adapters.qq.models import MessageMarkdown, MessageMarkdownParams


class MarkdownBuilder:
    CUSTOM_TEMPLATE_ID = ""  # 固定md模板id或手动传入

    @classmethod
    def markdown(cls, content_or_params, template_id: str = None):
        """
        构建 Markdown 消息段。
        - 传入 str：自定义原生MD
        - 传入 dict：模板MD
        :param content_or_params: str 或 dict
        :param template_id: 模板ID，传入时强制使用模板MD
        """
        tid = template_id or cls.CUSTOM_TEMPLATE_ID

        if isinstance(content_or_params, dict) and tid:
            # 模板MD
            markdown_params = []
            for key, values in content_or_params.items():
                if not isinstance(values, list):
                    values = [values]
                markdown_params.append(MessageMarkdownParams(key=key, values=values))

            markdown_message = MessageMarkdown(
                custom_template_id=tid,
                params=markdown_params
            )

        elif isinstance(content_or_params, str):
            # 原生MD
            markdown_message = MessageMarkdown(content=content_or_params)

        else:
            raise TypeError("参数错误，请传入 str使用原生Markdown或 dict + template_id使用模板Markdown")

        return MessageSegment.markdown(markdown_message)
