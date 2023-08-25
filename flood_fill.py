class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        rows = len(image)
        cols = len(image[0])
        to_be_filled = {(sr, sc)}
        old_color = image[sr][sc]

        if old_color == color:
            return image

        while to_be_filled:
            r, c = to_be_filled.pop()

            if 0 <= r < rows and 0 <= c < cols and image[r][c] == old_color:
                image[r][c] = color

                neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                for neighbor in neighbors:
                    if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                        to_be_filled.add(neighbor)

        return image
