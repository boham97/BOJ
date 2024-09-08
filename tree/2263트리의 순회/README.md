                            1

                2                3

        4            5    6            7

inorder: 4 2 5 1 6 3 7

post: 4 5 2 6 7 3 1

post order를 통해 1이 root임을 알 수 있다

1을 중심으로 inorder의 좌우가 각각 왼쪽 서브 트리 오른쪽 서브트리의 노드임을 알수있다

4 2 5 inorder

4 5 2 postorder

postorder마지막인 2를 통해 1의 왼쪽자식이 2임을 알수있다

4와 5는 각각 왼쪽 오른쪽 서브트리 길이가 1이므로 좌우 자식

이진탐색처럼 범위를 줄여나가자



left right 범위가 다르다
