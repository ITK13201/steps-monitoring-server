import io
import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import japanize_matplotlib

JST = datetime.timezone(datetime.timedelta(hours=+9), "JST")


def plt2svg() -> bytes:
    buf = io.BytesIO()
    plt.savefig(buf, format="svg", dpi=300)
    binary = buf.getvalue()
    buf.close()
    return binary


def plot_figure(x: list, y: list, xlabel: str, ylabel: str) -> bytes:
    ax = plt.subplot()
    ax.bar(x, y)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Formatterでx軸の日付ラベルを月・日に設定
    xfmt = mdates.DateFormatter("%m/%d")
    # DayLocatorで間隔を日数に
    xloc = mdates.DayLocator()
    ax.xaxis.set_major_locator(xloc)
    ax.xaxis.set_major_formatter(xfmt)
    ax.set_xlim(x[0] + datetime.timedelta(days=-1), x[-1] + datetime.timedelta(days=1))
    ax.grid(True)

    fig = plt2svg()
    plt.cla()
    return fig
