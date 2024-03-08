from iteung import reply
import numpy as np

message = input("Kamu: ")
return_message, status,dec_outputs = reply.botReply(message)
print(f"ITeung: {return_message}")


sampled_word_index = np.argmax(dec_outputs[0, -1, :])
print(dec_outputs[0, -1, sampled_word_index])