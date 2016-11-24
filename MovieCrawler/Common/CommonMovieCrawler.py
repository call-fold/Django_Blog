#!/usr/bin/env python
# -*- coding: utf-8 -*-
from MovieCrawler.Common.CrawlerToHTML import get_title_from_html, get_links_from_html_keyword


def get_movie_download_tuple(url, decode_type='utf-8'):
    movie_title = get_title_from_html(url, decode_type)
    download_link_list = get_movie_download_link(url, decode_type)
    return movie_title, download_link_list[0]


def get_movie_download_link(url, decode_type='utf-8'):
    download_link_list = get_links_from_html_keyword(url, 'ftp', decode_type)
    # print(url)
    return download_link_list[0]


def get_movie_download_list(real_movie_link_list, decode_type='utf-8', if_add_title=True):
    movie_download_list = []
    for real_movie_link in real_movie_link_list:
        if if_add_title:
            movie_download = get_movie_download_tuple(real_movie_link, decode_type)
        else:
            movie_download = get_movie_download_link(real_movie_link, decode_type)
        movie_download_list.append(movie_download)
    return movie_download_list
