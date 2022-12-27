### 이건 나중에 시각화 할 때,
### 로직으로 쓰면 됨!


## 여기에 있는 데이터로 가져와서..!
data = pd.read_csv('대표군집클러스터링.csv', encoding='utf-8', index_col=0)
data = pd.read_csv('전체맥주클러스터링.csv', encoding='utf-8', index_col=0)


def show_cluster(result, name):
    categories = ['Aroma', 'Appearance', 'Flavor','Mouthfeel', 'Overall']
    color = ['skyblue', 'blue', 'salmon', 'green']

    target = result[result['맥주'] == name]
    cluster = target['Cluster'].iloc[0]
    target = target[categories]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r = c_result.values[0],
        theta = categories,
        fill='toself',
        name='Soso',
        line_color=color[0]
    ))

    fig.add_trace(go.Scatterpolar(
        r = c_result.values[1],
        theta = categories,
        fill='toself',
        name='Sad',
        line_color=color[1]
    ))

    fig.add_trace(go.Scatterpolar(
        r = c_result.values[2],
        theta = categories,
        fill='toself',
        name='Good',
        line_color=color[2]
    ))

    fig.add_trace(go.Scatterpolar(
        r = target.values[0],
        theta = categories,
        fill='toself',
        name=name,
        line_color=color[3]
    ))

    fig.update_layout(
        polar=dict(
        radialaxis=dict(
            visible=True,
        )),
    )

    fig.show()

# 클라우드 맥주 클러스터링 결과
show_cluster(result, 'Kloud Original Gravity')