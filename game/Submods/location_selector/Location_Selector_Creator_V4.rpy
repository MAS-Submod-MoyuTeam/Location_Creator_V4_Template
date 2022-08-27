init -1 python:
    if not store.mas_submod_utils.isSubmodInstalled("房间模板V4核心"):
        raise Exception("\n\n\n\n本模组需要‘房间模板V4核心’作为前置子模组\n\n\n\n")
    store.LocationManager.AddLocation(
        LocationData(
            # 房间id，这个id不能重复
            "Location_Creator_V4_template",
            # 选择时显示的房间名称
            "房间模板V4",
            # 房间图片列表
            # 需要填写对应的图片路径，可以通过config设置项添加路径前缀
            # 所有图片大小必须为1280*720 建议使用PS处理透明图层
            # 除了白天def和夜间def，其它都可以删除或留None
            {
                # 白天
                "day":{
                    # 晴朗 - 此项必填
                    'def': "Location_Template_Simple_d.png",
                    # 下雨
                    'rain':None,
                    # 多云
                    'overcast':None,
                    # 下雪
                    'snow':None
                },
                # 夜晚
                "night":{
                    # 晴朗 - 此项必填
                    'def':"Location_Template_Simple_n.png",
                    'rain':None,
                    'overcast':None,
                    'snow':None
                },
                # 落日
                "sunset":{
                    'def':None,
                    'rain':None,
                    'overcast':None,
                    'snow':None
                }
            },
            config={
                # 是否启用entry_pp
                'entry_pp_enable': False,
                # 是否启用exit_pp
                'exit_pp_enable': False,
                # 进入房间时的聊天内容 格式为(1eua, "要说的话")
                'entry_talk': None,
                # 回到太空教室时的聊天内容
                'exit_talk': None,
                # 更换桌面，文件应该位于mod_assets/monika/t，命名格式为 table-<desk_acs的值>.png，需要启用entry_pp和exit_pp
                'desk_acs': None,
                # 更换椅子，文件应该位于mod_assets/monika/t，命名格式为 chair-<chair_acs的值>.png，需要启用entry_pp和exit_pp
                'chair_acs': None,
                # 图片路径前置
                'location_assets_prefix':"mod_assets/location/Location_Creator/"
            },
            setting={
                # 禁用天气变换
                'disable_progressive': False,
                # 禁用天气动画
                'hide_masks': False,
                # 隐藏日历
                'hide_calendar': True,
                # 解锁状态
                'unlocked': True,
                # 进入房间时会执行一次entry_pp，需要打开config中对应的enable
                'entry_pp': None,
                # 离开房间后会执行一次exit_pp，需要打开config中对应的enable
                'exit_pp': None,
                # 额外属性
                'ex_props': None,
                # MASDecoManager 应该是特定节日的装饰管理器
                'deco_man': None
            }
        )
    )
