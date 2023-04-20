from django.shortcuts import render, HttpResponse
from django.http import Http404

pages = [
    '''Hiking can be a great way to get exercise, enjoy nature, and relieve stress, but it's not without its dangers. One of the biggest risks associated with hiking is the potential for accidents or injuries. Hikers can fall, trip, or slip on wet or uneven terrain, and these accidents can lead to broken bones, sprains, or even more serious injuries. Hikers can also become lost or stranded in remote areas, which can put them in danger of exposure, dehydration, or starvation.

Another danger of hiking is the potential for encounters with wildlife. While most wildlife encounters are relatively harmless, some animals, such as bears, mountain lions, and snakes, can be dangerous if provoked or surprised. Hikers should always be aware of their surroundings and take steps to avoid interactions with wildlife. This may include carrying bear spray or other deterrents, making noise to alert animals to your presence, and keeping a safe distance from any wildlife you encounter.

Finally, weather can also pose a danger to hikers. Thunderstorms can bring lightning strikes and flash floods, while extreme heat or cold can lead to heat exhaustion or hypothermia. Hikers should always check the weather forecast before heading out and be prepared for any conditions they may encounter. This may include carrying appropriate clothing, food, and water, as well as a map and compass or GPS device to help navigate in case of unexpected weather or trail conditions. Overall, while hiking can be a wonderful way to explore the great outdoors, it's important to be aware of the potential dangers and take steps to stay safe.''',
    'Marriage is a beautiful institution that brings two individuals together in a bond of love, commitment, and companionship. It is a journey that involves mutual understanding, respect, and support for each other through the highs and lows of life. The beauty of marriage lies in the fact that it provides a platform for two people to share their joys, sorrows, dreams, and aspirations with each other. It is a partnership that allows individuals to grow together, learn from each other, and create a life that is filled with love, happiness, and contentment. The journey of marriage is not always smooth, but the beauty of it lies in the fact that the challenges are overcome together, making the bond even stronger. Ultimately, the beauty of marriage lies in the unbreakable bond that two individuals share, a bond that is built on love, trust, and commitment, and lasts a lifetime.',
    '''Eating is a beautiful experience that engages all our senses, from the sight of a colorful plate to the aroma of freshly cooked food and the taste of each bite. It is not only a necessity for survival but also a source of pleasure and joy. The beauty of eating lies in the diversity of flavors, textures, and cuisines that are available around the world. Sharing a meal with loved ones is a beautiful way to bond and connect with each other, and it can bring a sense of comfort and happiness.'''
]

def index(request, page_nr):
    return render(request, 'lorem/index.html', { 'page_nr': page_nr })

def text(request, page_nr):
    try:
        return HttpResponse(pages[page_nr])
    except IndexError:
        raise Http404()
