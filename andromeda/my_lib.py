# import vizible
# vizible.func()
# import cowsay
# cowsay.tux('Hello World')
# print(cowsay.get_output_string('trex', 'Hello (extinct) World'))
# cowsay.dragon('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris blandit rhoncus nibh. Mauris mi mauris, molestie vel metus sit amet, aliquam vulputate nibh.')
from progress.bar import Bar,ChargingBar,FillingSquaresBar
import time
def download():
    bar = FillingSquaresBar('Загрузка', max=20)
    for i in range(20):
        bar.next()
        time.sleep(0.1)
    bar.finish

import emoji
print(emoji.emojize('Меня зовут Степан :OK_hand:'))


