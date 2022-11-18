categories = _.columns

# restaurant_1 = [4, 4, 5, 4, 3]
# restaurant_2 = [5, 5, 4, 5, 2]
# restaurant_3 = [3, 4, 5, 3, 5]

categories = _.loc['2022-10-25 18:00:00+08:00'].sort_values()[-6:].index

_mean = list(map(lambda it: it, _.loc['mean'][categories].values))
_25_percent = list(map(lambda it: it, _.loc['25%'][categories].values))
_50_percent = list(map(lambda it: it, _.loc['50%'][categories].values))
_75_percent = list(map(lambda it: it, _.loc['75%'][categories].values))
_max = list(map(lambda it: it, _.loc['max'][categories].values))

label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(_mean))

plt.figure(figsize=(5, 5))
plt.subplot(polar=True)

_labels = [('mean', _mean)
          , ('25%', _25_percent)
          , ('50%', _50_percent)
          , ('75%', _75_percent)]
for (n, l) in _labels:
    plt.plot(label_loc, l, label=n, alpha=0.3)
plt.title('Restaurant comparison', size=20)
lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
plt.legend()
plt.show()
