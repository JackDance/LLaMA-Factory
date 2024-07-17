# !/usr/bin/env python
# coding=utf-8

"""
@author: Jack
@license: MIT
@contact: jack_zhangluyao@163.com
@file: DPO_convert2sharegpt_format.py
@date: 2024/7/17 14:55
@desc: 
"""
import json

def convert2sharegpt_format(src_json_path:str, dst_json_path:str):
    """
    :param src_json_path:
    :param dst_json_path:
    result:
    """
    converted_json_list = []
    with open(src_json_path, 'r', encoding='utf-8') as f:
        for line in f:
            conversation_dict = {}
            data = json.loads(line)
            conversation_dict["conversations"] = [{"from":"human", "value":data["question"]}]
            conversation_dict["chosen"] = {"from":"gpt", "value":data["response_chosen"]}
            conversation_dict["rejected"] = {"from":"gpt", "value":data["response_rejected"]}
            converted_json_list.append(conversation_dict)

    with open(dst_json_path, 'w', encoding='utf-8') as f:
        json.dump(converted_json_list, f, ensure_ascii=False, indent=4)
    print("Converted Successfully!")



if __name__ == '__main__':
    src_json_path = '/Users/luyaozhang/Desktop/test/src/dpo_zh_universe.jsonl'
    dst_json_path = '/Users/luyaozhang/Desktop/test/dst/dpo_zh_universe.jsonl'
    convert2sharegpt_format(src_json_path, dst_json_path)

