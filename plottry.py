from matplotlib import pyplot as plt
import scraper


pp, score_date = scraper.main()

print(pp)
print(score_date)




plt.plot(pp, score_date)

plt.show()

