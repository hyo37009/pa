from linePrepare import line3, line4, line7

def search(st, end, line):
    lines = [line3, line4, line7]

    if st.line & end.line:
        # 시작역과 도착역이 같은 노선인 경우
        route = [st, end]
        return route

    else:
        # 시작역과 도착역이 다른 노선인 경우
        # 환승역을 찾습니다
        hwanLine = list(end.line)[0]
        hwanSt = []
        for linenum in lines:
            if linenum.linename == hwanLine:
                hwanLine = linenum

        for station in hwanLine.linelist:
            if station.hwan:
                if (st.line | end.line) == station.line:
                    hwanSt.append(station)

        if len(hwanSt) == 1:
            route = [st, hwanSt[0], end]
            return route
        else:
            far = []
            for hwan in hwanSt:
                first = line.howfar(st, line.ret_station(hwan.name))
                sec = hwanLine.howfar(hwanLine.ret_station(hwan.name), end)
                # far.append(line.howfar(st, hwan) + hwanLine.howfar(hwan, end))
                far.append(first+sec)
            hwanSt = hwanSt[far.index(min(far))]
            return [st, hwanSt, end]

if __name__ == '__main__':

    route = search(line3.ret_station('대화'), line7.ret_station('논현'), line3)
    print(route)


