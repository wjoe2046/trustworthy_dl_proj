import json

with open("train.json") as json_file:
    qna_data = json.load(json_file)

with open("test_output.txt", "w") as txt_file:
    for item in qna_data:
        txt_file.write("Context: {}\n".format(item["context"]))
        txt_file.write("Question: {}\n".format(item["question"]))
        txt_file.write("Answer: {}\n".format(item["answers"]))
        txt_file.write("Label: {}\n\n".format(item["label"]))
