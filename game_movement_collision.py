import pygame
import sys

# 初始化pygame
pygame.init()

# 游戏窗口设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("角色移动与碰撞检测示例")

# 颜色定义
WHITE = (255, 255, 255)
RED = (255, 0, 0)    # 角色颜色
BLUE = (0, 0, 255)   # 障碍物颜色
BLACK = (0, 0, 0)    # 文本颜色

# 角色类
class Player:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.color = RED
        
    def move(self, dx, dy, obstacles):
        # 先尝试在x方向移动
        self.rect.x += dx
        # 检查x方向是否碰撞
        if self.check_collision(obstacles):
            self.rect.x -= dx
            
        # 再尝试在y方向移动
        self.rect.y += dy
        # 检查y方向是否碰撞
        if self.check_collision(obstacles):
            self.rect.y -= dy
            
    def check_collision(self, obstacles):
        # 检查与所有障碍物是否碰撞
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                return True
        return False
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# 障碍物类
class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BLUE
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# 创建游戏对象
def create_objects():
    # 创建玩家
    player = Player(50, 50, 40, 40, 5)
    
    # 创建障碍物
    obstacles = [
        Obstacle(200, 100, 100, 30),
        Obstacle(400, 200, 30, 100),
        Obstacle(100, 300, 150, 30),
        Obstacle(500, 400, 100, 30),
        Obstacle(300, 500, 30, 80)
    ]
    
    return player, obstacles

# 主游戏循环
def main():
    clock = pygame.time.Clock()
    player, obstacles = create_objects()
    
    # 字体设置
    font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 获取按键状态
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        
        # 移动控制
        if keys[pygame.K_LEFT]:
            dx = -player.speed
        if keys[pygame.K_RIGHT]:
            dx = player.speed
        if keys[pygame.K_UP]:
            dy = -player.speed
        if keys[pygame.K_DOWN]:
            dy = player.speed
            
        # 移动角色并检测碰撞
        player.move(dx, dy, obstacles)
        
        # 绘制
        screen.fill(WHITE)
        player.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)
            
        # 显示提示文本
        text = font.render("使用方向键移动角色", True, BLACK)
        screen.blit(text, (10, 10))
        
        # 刷新屏幕
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
