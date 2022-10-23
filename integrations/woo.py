from woocommerce import API


def get_woo_api(url, ck, cs):


    wcapi = API(
        url=url,
        consumer_key=ck,
        consumer_secret=cs,
        version="wc/v3",
        timeout=60
    )

    return wcapi
