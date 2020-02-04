import requests
import time
import concurrent.futures as futures
from bench import bench

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    # 'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    # 'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    # 'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    # 'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    # 'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    # 'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    # 'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    # 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    # 'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    # 'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    # 'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    # 'https://images.unsplash.com/photo-1550439062-609e1531270e',
    # 'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]


def _download_image(img_url):
    img_bytes = requests.get(img_url).content
    print(f'{img_url} was downloaded...')
    return img_bytes


def _write_to_file(file_path, data, mode='wb'):
    with open(file_path, mode) as file:
        file.write(data)
        print(f'{file_path} was written to file...')


def _download_and_save_image(img_url):
    img_bytes = _download_image(img_url)

    img_name = img_url.split('/')[3]
    img_path = f'img/{img_name}.jpg'

    _write_to_file(img_path, img_bytes, "wb")


# TODO: FIND: if there's any benefit by using this func
def _download_and_save_image2(img_url):
    with futures.ThreadPoolExecutor() as executor:
        f = executor.submit(_download_image, img_url)
        img_bytes - f.result()

        img_name = img_url.split('/')[3]
        img_path = f'img/{img_name}.jpg'

        f = executor.submit(_write_to_file, img_path, img_bytes, "wb")


def download_sequential():
    for url in img_urls:
        _download_and_save_image(url)


def download_using_threads():
    with futures.ThreadPoolExecutor() as executor:
        # executor.map(_download_and_save_image, img_urls)

        # fs = [executor.submit(_download_and_save_image, url) for url in img_urls]
        fs = [executor.submit(_download_and_save_image2, url)
              for url in img_urls]

        for f in futures.as_completed(fs):
            print(f)


def download_using_processes():
    with futures.ProcessPoolExecutor() as executor:
        executor.map(_download_and_save_image, img_urls)


if __name__ == "__main__":
    t1 = time.perf_counter()

#     download_sequential()
    download_using_threads()
    # download_using_processes()

    t2 = time.perf_counter()

    print(f'Finished in {t2-t1} seconds')
