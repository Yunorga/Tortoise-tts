# Imports used through the rest of the notebook.
import datetime

def print_time_elapsed(message):
  """Affiche le temps courant avec une précision à la seconde.
  """
  now = datetime.datetime.now()
  print(f"{message} = \033[91m {now:%M:%S} \033[0m")

print_time_elapsed("start import")
import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F

print_time_elapsed("end import Torch")

from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices

print_time_elapsed("end import TorToiSe")

import time
import os


print_time_elapsed("end import OS")
print("..............")
print_time_elapsed("start def tts")
# This will download all the models used by Tortoise from the HuggingFace hub.
tts = TextToSpeech()
print_time_elapsed("end def tts")
print("..............")
# This is the text that will be spoken.
# text = "Hi, it's me Emmanuel, how are you today ? Me ? I'm fine because of you"
# Pick a "preset mode" to determine quality. Options: {"ultra_fast", "fast" (default), "standard", "high_quality"}. See docs in api.py
preset = "ultra_fast"

# Load it and send it through Tortoise.
# voice_samples, conditioning_latents = load_voice(voice)
# gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents, 
#                           preset=preset)
def gen(text,voice):
    voice_samples, conditioning_latents = load_voice(voice)
    gen = tts.tts(text=text,
              voice_samples=voice_samples,
              conditioning_latents=conditioning_latents,
              temperature=0.8,
              length_penalty=1.0,
              repetition_penalty=2.0,
              top_p=0.8,
              cond_free_k=2.0,
              diffusion_temperature=1.0,
              num_autoregressive_samples=1,
              diffusion_iterations=7,
              cvvp_amount=0,
              k=1)
    
    print_time_elapsed("Gen complete")
    leTemps = time.time()


    paths = [] # Listes des chemins du/des fichier(s) générés

    # We save the generated audio file, and the function return the path if the file
    os.makedirs(f'./static/audio/generated/{voice}', exist_ok=True)

    if isinstance(gen, list):
        for j, g in enumerate(gen):
            paths.append(f'./static/audio/generated/{voice}/{voice}_{j}_{leTemps}_.wav')
            torchaudio.save(paths[-1], g.squeeze(0).cpu(), 24000)
    else:
        paths.append(f'./static/audio/generated/{voice}/{voice}_{leTemps}_.wav')
        torchaudio.save(paths[-1], gen.squeeze(0).cpu(), 24000)
    return f'/static/audio/generated/{voice}/{voice}_{leTemps}_.wav'

    # torchaudio.save(f'../results/generated_{voice}.wav', gen.squeeze(0).cpu(), 24000)
    # return f'../results/generated_{voice}.wav'


    # ADD if multiples audio files need to be generated
    #
    # if isinstance(gen, list):
    #     for j, g in enumerate(gen):
    #         torchaudio.save(os.path.join(args.output_path, f'{selected_voice}_{k}_{j}.wav'), g.squeeze(0).cpu(), 24000)
    # else:
    #     torchaudio.save(os.path.join(args.output_path, f'{selected_voice}_{k}.wav'), gen.squeeze(0).cpu(), 24000)
print_time_elapsed("start gen")
chemin = gen("Hi I'm French","trump")
print_time_elapsed("end gen")
print("chemin : ",chemin)