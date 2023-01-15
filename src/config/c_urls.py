urls = {
    "playlist": {
        "head": "https://yesplaymusic.yunyuwu.cn/api/top/playlist?cat=%E5%85%A8%E9%83%A8&offset=",
        "offset": 96,  # start num
        "limit": "&limit=48"
    },
    "song_detail": {
        "head": "https://yesplaymusic.yunyuwu.cn/api/song/detail?ids=",
        "ids": ""
    },
    "lyric": {
        "head": "https://yesplaymusic.yunyuwu.cn/api/lyric?id=",
        "id": ""
    },
    "personal_fm": {
        "head": "https://yesplaymusic.yunyuwu.cn/api/personal_fm?timestamp=",
        "timestamp": ""
    }
}
# 歌单 -- 歌曲 -- 歌手
# 歌曲中判断是否可以使用，
# pl song singer 三张基础表
# user u_like_list user_message
