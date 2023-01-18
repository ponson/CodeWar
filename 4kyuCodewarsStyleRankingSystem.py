class User():

    ranks = (-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8)

    def __init__(self) -> None:
        self.rank = -8
        self.progress = 0

    def add_points(self, diff):
        if diff == 0:
            self.progress += 3
        elif diff == -1:
            self.progress += 1
        elif diff > 0:
            self.progress += (10 * diff * diff)

    def upgrade_rank(self):
        if self.rank == 8 or self.progress < 100:
            return

        cur_idx = User.ranks.index(self.rank)
        while self.progress >= 100 and self.rank < 8:
            cur_idx += 1
            self.rank = User.ranks[cur_idx]
            self.progress -= 100

        if self.rank == 8:
            self.progress = 0

    def rank_process(self, d_rank):
        self.add_points(d_rank)
        self.upgrade_rank()
        pass

    def inc_progress(self, done_activity_rank):
        # try:
        #     User.ranks.index(done_activity_rank)
        # except:
        #     print("Invalid rank.")

        if done_activity_rank not in User.ranks:
            raise ValueError()

        if self.rank == 8:
            self.progress = 0
        else:
            diff_rank = User.ranks.index(
                done_activity_rank) - User.ranks.index(self.rank)
            self.rank_process(diff_rank)

user = User()
print(user.rank)
print(user.progress)
print(user.inc_progress(-7))
print(user.progress)
print(user.inc_progress(-8))
print(user.progress)
print(user.rank)