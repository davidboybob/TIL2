import socket
import time
import math

# User and Game Server Information
NICKNAME = 'PAK SUNG JIN'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    angle, power = 0, 0
    print('if gameData.balls == {}: angle, power = {}, {}'.format(gameData.balls, angle, power))
    if gameData.balls == [[65, 65], [125, 120], [0, 0], [0, 0], [0, 0]]: angle, power = 50, 55
    if gameData.balls == [[65, 65], [250, 10], [0, 0], [0, 0], [0, 0]]: angle, power = 105, 110
    if gameData.balls == [[65, 65], [250, 10], [15, 10], [0, 0], [0, 0]]: angle, power = 105, 110
    if gameData.balls == [[220, 33], [0, 0], [15, 10], [0, 0], [0, 0]]: angle, power = 265, 120
    if gameData.balls == [[65, 65], [125, 120], [240, 124], [250, 10], [0, 0]]: angle, power = 50, 55
    if gameData.balls == [[154, 121], [0, 0], [240, 124], [250, 10], [0, 0]]: angle, power = 88, 63
    if gameData.balls == [[254, 124], [0, 0], [0, 0], [250, 10], [0, 0]]: angle, power = 185, 82
    if gameData.balls == [[65, 65], [195, 65], [0, 0], [0, 0], [0, 0]]: angle, power = 91, 140
    if gameData.balls == [[237, 50], [237, 64], [0, 0], [0, 0], [0, 0]]: angle, power = -17, 70
    if gameData.balls == [[174, 119], [251, 121], [0, 0], [0, 0], [0, 0]]: angle, power = 93, 70
    if gameData.balls == [[65, 65], [195, 65], [203, 57], [203, 73], [211, 65]]: angle, power = 91, 200
    if gameData.balls == [[250, 44], [248, 85], [234, 24], [233, 111], [232, 60]]: angle, power = 355, 80
    if gameData.balls == [[234, 121], [0, 0], [234, 24], [224, 122], [232, 60]]: angle, power = 200, 35
    if gameData.balls == [[207, 46], [0, 0], [234, 24], [224, 122], [232, 60]]: angle, power = 128, 50
    if gameData.balls == [[252, 12], [0, 0], [0, 0], [224, 122], [232, 60]]: angle, power = 350, 80
    if gameData.balls == [[227, 86], [0, 0], [0, 0], [221, 119], [232, 60]]: angle, power = 340, 40
    if gameData.balls == [[191, 111], [0, 0], [0, 0], [222, 119], [232, 60]]: angle, power = 65, 60
    if gameData.balls == [[243, 99], [0, 0], [0, 0], [250, 115], [232, 60]]: angle, power = 18, 30
    if gameData.balls == [[247, 121], [0, 0], [0, 0], [0, 0], [232, 60]]: angle, power = 195, 50
    if gameData.balls == [[220, 44], [0, 0], [0, 0], [0, 0], [228, 29]]: angle, power = 172, 80
    if gameData.balls == [[207, 61], [0, 0], [0, 0], [0, 0], [252, 7]]: angle, power = 140, 40




    ######################################################################################
    # 주어진 정보를 바탕으로 샷을 할 방향과 세기를 결정해서 angle, power 값으로 지정 #
    ######################################################################################
    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        if gameData.balls[0][0] == 9909:
            break
        play(conn, gameData)
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
