class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (start_index, height) — 아직 안 끊긴 가로선들

        for i, h in enumerate(heights):
            start = i

            # TODO 1: 스택 top의 가로선이 현재 막대 h에 "부딪히는" 조건은?
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()

                # TODO 2: 끊긴 가로선의 넓이 = 높이 × 폭
                #         폭은 어디서부터 어디까지?
                area = height * (i - idx)
                max_area = max(max_area, area)

                # TODO 3: 현재 막대는 왼쪽으로 어디까지 뻗을 수 있나?
                start = idx

            stack.append((start, h))

        # TODO 4: 끝까지 안 끊긴 가로선들은 어디까지 뻗었나?
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        
        return max_area