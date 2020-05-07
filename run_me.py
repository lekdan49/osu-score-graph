from matplotlib import pyplot as plt

import scraper


def set_sizes():
    fig_size = plt.rcParams["figure.figsize"]
    # print("Current size:", fig_size)  # prints default res witch is 640 x 480
    fig_size[0] = 20  # sets resolution on x axis to 2000
    fig_size[1] = 6.4  # sets resolution on y axis to 640
    # print("Current size:", fig_size)  # prints current resolution which is 2000 x 640

    plt.tick_params(axis='x', which='major', labelsize=5)  # change x axis font
    plt.tick_params(axis='x', which='minor', labelsize=4)  # change x axis font


def plot_graph(pp1, score_date2, user_name1):
    plt.style.use('fivethirtyeight')
    plt.plot(pp1, score_date2, label=user_name1[0], marker='.', linewidth=2.0)  # plots the graph

    plt.title('PP scores over time for top 50 scores ')
    plt.xlabel('Date of score ')
    plt.ylabel('PP value ')
    plt.legend()  # actually print the legend
    plt.grid('on', linestyle='--')
    plt.tight_layout()
    png_saved = user_name1[0] + '.png'
    svg_saved = user_name1[0] + '.svg'

    plt.savefig(png_saved, dpi=300)  # saves pp graph as .png
    plt.savefig(svg_saved)  # saves an svg
    plt.show()


def main():
    pp1, score_date2, user_name1 = scraper.main()

    pp1, score_date2 = zip(*sorted(zip(score_date2, pp1)))  # sorts dates and pp

    # print(pp1)
    # print(score_date2)

    set_sizes()
    plot_graph(pp1, score_date2, user_name1)


if __name__ == '__main__':
    main()
