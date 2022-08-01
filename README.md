# FisherHunter 
## FFXIV钓鱼欺诈网站汉化捕捉器ACT高级触发器脚本

*本工具仅限于FFXIV中国服使用（那就不写英文说明了……*

## 前言

帐号诈骗的钓鱼网站骗子在游戏里喊话，已经不是一天两天的事了，至于是运营管理不作为还是骗子的生生不息，不想再深究了，老爹说：用魔法打败魔法，所以我们整点幻想科技来自主净化我们的游戏生活视野。

2020年时nga一位大兄弟曾经牵头动用LOIC打击钓鱼网诈骗网站，并逐步更新方案，一直奋战到了2021年，此后不知道是因为收集服务器被报复性攻击，还是受限个人成本打击资源耗尽，此后这位大兄弟销声匿迹，但他和他的小伙伴为我们留下了一套实现方案：运用ACT的act的Triggernometry高级触发器在游戏内捕获骗子的喊话信息，并将捕获的诈骗网站导入打击服务器实现自动化打击。



## 优化

基于这个设计方案，在熟练使用Triggernometry插件朋友的帮助下，我构建了新的喊话捕获脚本，由于原插件脚本的明文传参公开性会导致接受服务器地址被曝光，故这边采用了[Bluefissure](https://github.com/Bluefissure)的[OtterBot](https://github.com/Bluefissure/OtterBot)方案进行采集信息转发，对服务器地址进行了保护。

但为了防止对诈骗网站的打击策略受到防范，以及回避报复性打击，此处仅提供Triggernometry脚本部分供光之战士们使用，打击服务器源代码在骗子被彻底治服前将不开源。



## 使用依赖

FFXIV ACT国服版：

- [**CafeACT整合**](https://ngabbs.com/read.php?tid=17412506)
- [**ACT.呆萌整合**](https://ngabbs.com/read.php?tid=19019884)

Triggernometry（高级触发器）

- 请于ACT插件中心中进行安装并启用



## 使用方法

在Triggernometry插件的远程触发器组中，以仓库方式导入[**FisherHunter.xml**](https://github.com/NyaaCaster/FisherHunter/releases/download/FisherHunter/FisherHunter.xml)的文件链接，并启用【钓鱼网站喊话捕获器】触发器，

导入完成后，如在游戏过程中遇到骗子的喊话，将触发act的tts语音提示(可关闭该语音提示)，

此后触发器将自动上报捕获的诈骗网站信息，打击服务器收到上报后将自动进行打击处理。

以远程触发器方式导入，可获得本触发器脚本的在线实时更新。


## 注意事项

1. FFXIV ACT是一款未经FFXIV游戏研发方及运营授权许可的第三方辅助工具，本工具使用过程中会未经游戏研发和运营商许可擅自调用解析游戏内容数据（俗称*挂），请静默使用，不要进行大张旗鼓的宣扬
2. 不使用ACT工具或不会使用Triggernometry插件的朋友，可以将看到的骗子喊话内容发送到此nga帖进行收集：https://bbs.nga.cn/read.php?tid=32849504
3. 本采集工具不会收集任何信息(包括且不限于游戏内外信息)
4. “虽然装上这个触发器，除了收集钓鱼网站信息，你无法从中获得任何可见好处和收益，但是我为大家无私助力于肃清艾欧泽亚邪恶势力所做的努力致以崇高的敬意！”  ——某位光之战士
5. 迫于打击资源有限，请勿投喂无效信息，我们打击骗子，请勿打击我



## TODO

- 传参封装化
