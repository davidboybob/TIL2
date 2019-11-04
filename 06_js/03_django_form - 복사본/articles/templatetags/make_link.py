from django import template

register = template.Library()

@register.filter
def hashtag_link(word):
    # word는 article 객체가 들어갈 건데
    # article의 content 들만 모두 가져와서 그 중 해시태그에만 링크를 붙인다.
    # {{ article|hashtag_link }}

    content = word.content + ' '
    hashtags = word.hashtags.all()

    for hashtag in hashtags:
        #cotent = .replace(과거내용, 변경내용)
        content = content.replace(hashtag.content + ' ', f'<a href="/articles/{hashtag.pk}/hashtag/" class="text-primary">{hashtag.content}</a> ') # 마지막 공백(스페이스) 중요 !! #html a태그를 씌운 것으로 바꿈)
    return content