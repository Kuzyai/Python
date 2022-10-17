from pytube import YouTube
youtube_video_url = 'https://youtu.be/8dJyRm2jJ-U'
choice = input('''1. Загрузка видео.
2. Загрузка аудио из видео.
Выберете пункт: -> ''')
try:
    if choice == '1':
        yt_obj = YouTube(youtube_video_url)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        filters.get_highest_resolution().download(
            output_path='C:\\Users\\ognev\\Desktop')
        print(f'Video Title is {yt_obj.title}')
        print(f'Video Length is {yt_obj.length} seconds')
        print(f'Video Description is {yt_obj.description}')
        print(f'Video Rating is {yt_obj.rating}')
        print(f'Video Views Count is {yt_obj.views}')
        print(f'Video Author is {yt_obj.author}')
        print('Video Downloaded Successfully')
    elif choice == '2':
        yt_obj = YouTube(youtube_video_url)
        yt_obj.streams.get_audio_only().download(
            output_path='C:\\Users\\ognev\\Desktop')
        print('YouTube video audio downloaded successfully')
except Exception as e:
    print(e)
