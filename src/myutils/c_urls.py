urls = {
    "playlist": {
        # https://yesplaymusic.yunyuwu.cn/api/top/playlist?cat=%E5%85%A8%E9%83%A8&offset=50
        "head": "https://yesplaymusic.yunyuwu.cn/api/top/playlist?cat=%E5%85%A8%E9%83%A8&offset=",
        "offset": 0,  # start num
        "limit": 50,
    },
    "playlist_detail": {
        "head": "https://yesplaymusic.yunyuwu.cn/api/playlist/detail?id=",
        "id": "",
        "timestamp": "&timestamp="
    },
    "song_detail": {
        "head": "https://yesplaymusic.yunyuwu.cn/api/song/detail?ids=",
        "ids": ""
    },
    "song_listen_able": {
        "head": "https://yesplaymusic.yunyuwu.cn/api/song/url?id=",
        "id": ""
    },
    # 每首歌曲中每段歌词出现的时间，用在滚动歌词界面
    "lyric": {
        "head": "https://yesplaymusic.yunyuwu.cn/api/lyric?id=",
        "id": ""
    },
    "personal_fm": {
        "head": "https://yesplaymusic.yunyuwu.cn/api/personal_fm?timestamp=",
        "timestamp": ""
    },
    "artist": {
        "head": "https://yesplaymusic.yunyuwu.cn/api/simi/artist?id=",
        "id": ""
    }
}
# 歌单 -- 歌曲 -- 歌手
# 歌曲中判断是否可以使用，
# pl song singer 三张基础表
# user u_like_list user_message
