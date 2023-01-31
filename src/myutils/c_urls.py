urls = {
    "playlist": {
        # https://yesplaymusic.yunyuwu.cn/api/top/playlist?cat=%E5%85%A8%E9%83%A8&offset=50
        "head": "http://localhost:3000/top/playlist/highquality?limit=100&before=",
        "before": 0  # start num
    },
    "playlist_detail": {
        "head": "http://localhost:3000/playlist/detail?id=",
        "id": "",
        "s": "&s="
    },
    "song_detail": {
        "head": "http://localhost:3000/song/detail?ids=",
        "id": ""
    },
    "song_url": {
        "head": "http://localhost:3000/song/url?id=",
        "id": ""
    },
    "song_listen_able": {
        "head": "http://localhost:3000/check/music?id=",
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
