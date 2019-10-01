# coding=utf-8

import sys

from dmg_record import Record
from lock_boss import Lock
from reserve import Reserve
from yobot_msg import Message


def yobot(cmd_list):
    txt_list = []
    if len(cmd_list) != 5:
        txt_list.append("100参数错误")
    else:
        func = Message.match(cmd_list[4])
        if func != 0:
            txt_list.append(Message.msg(func))
            return txt_list  # 后面不再运行
        func = Lock.match(cmd_list[4])
        if func != 0:
            lockboss = Lock(cmd_list[1:4])
            lockboss.lockboss(cmd_list[4], func)
            txt_list.extend(lockboss.txt_list)
            return txt_list  # 后面不再运行
        func = Record.match(cmd_list[4])
        if func != 0:
            report = Record(cmd_list[1:4])
            report.rep(cmd_list[4], func)
            txt_list.extend(report.txt_list)
            if func == 3 or func == 4:
                pass  # 后面可能继续运行
            else:
                return txt_list  # 后面不再运行
        func = Reserve.match(cmd_list[4])
        if func != 0:
            rsv = Reserve(cmd_list[1:4])
            rsv.rsv(cmd_list[4], func)
            txt_list.extend(rsv.txt_list)
            return txt_list  # 后面不再运行
    if txt_list == []:
        txt_list.append("101无效命令")
    return txt_list


if __name__ == "__main__":
    txtlist = yobot(sys.argv)  # 获得输出文本的list
    print("\n".join(txtlist))  # 随便怎么用，这里直接连接并输出