from random import randrange
# 使用生成式生成10个用户，每个用户有3到9部电影的评分
data = {'用户' + str(i):{"电影"+str(randrange(1,15)):randrange(1,6) for j in range(randrange(3,10))}for i in range(10)}
user = {'电影'+str(randrange(3,9)):randrange(1,6) for j in range(6)}
def diff_value(username,filmname):
    score = 0
    for x in filmname:
        score = score + abs(data[username][x] - user[x])
    return score
def main():
    print("模拟历史电影数据".center(50,'-'))
    for lusername in data.keys():
        print("{} {}".format(lusername,data[lusername]))
    print('模拟当前用户电影数据'.center(50,'-'),'\n',user)
    film_count=0#共同评分电影
    film_user=''#评分最相近的用户
    film_score = 0#评分差值
    for key , value in data.items():
        film=set(value) & set(user)#交集,都评分过的电影
        if len(film) == film_count:#如果评分过的电影与已经记录的相同，那就比较分数
            if diff_value(key,film) < film_score:#与现在评分差的比较，如果评分的电影一样，但是分数差更小就进行替换
                film_count=len(film)#替换一起评分过的电影，其实这里并不需要，因为这里的判断条件是评分电影相同
                film_user=key#替换评分最近的用户
                film_score=diff_value(key,film)#替换评分差最小值
        if len(film) > film_count:#一起评分过的电影要比现在记录的要多
            film_count = len(film)  # 替换一起评分过的电影，其实这里并不需要，因为这里的判断条件是评分电影相同
            film_user = key  # 替换评分最近的用户
            film_score = diff_value(key, film)  # 替换评分差最小值
    print("电影评分值与当前用户评分相近的用户和对应电影是".center(50,'-'),'\n',film_user,data[film_user])
    set1 = set(data[film_user])
    set2 = set(user)
    max_score_filmnname = max(set1&set2,key=lambda x: data[film_user][x])#word代码中使用set1-set2,但是这样得到的最高分电影会出现用户没有评分过的电影，所以我使用交集，这样最后结果就是输出共同评分过，然后评分最高的电影
    print("评分最高的电影是".center(50,'-'),'\n',max_score_filmnname)
if __name__ == '__main__':
    main()