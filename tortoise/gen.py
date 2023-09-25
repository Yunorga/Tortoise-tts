# Imports used through the rest of the notebook.
import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F

from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices

import os
# This will download all the models used by Tortoise from the HuggingFace hub.
tts = TextToSpeech()

# This is the text that will be spoken.
text = "Hi, it's me Emmanuel, how are you today ? Me ? I'm fine because of you"
# Pick a "preset mode" to determine quality. Options: {"ultra_fast", "fast" (default), "standard", "high_quality"}. See docs in api.py
preset = "fast"


# Pick one of the voices from the output above
# voice = 'trump'

CUSTOM_VOICE_NAME = "macron"

custom_voice_folder = f"tortoise/voices/{CUSTOM_VOICE_NAME}"
voice_samples, conditioning_latents = load_voice(CUSTOM_VOICE_NAME)

# Load it and send it through Tortoise.
# voice_samples, conditioning_latents = load_voice(voice)
# gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents, 
#                           preset=preset)
def gen(text,voice):
    custom_voice_folder = f"tortoise/voices/{CUSTOM_VOICE_NAME}"
    voice_samples, conditioning_latents = load_voice(CUSTOM_VOICE_NAME)
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
              diffusion_iterations=24,
              cvvp_amount=0)

    torchaudio.save(f'../results/generated_{CUSTOM_VOICE_NAME}.wav', gen.squeeze(0).cpu(), 24000)

# CUSTOM_VOICE_NAME = "emma"


# custom_voice_folder = f"tortoise/voices/{CUSTOM_VOICE_NAME}"
# voice_samples, conditioning_latents = load_voice(CUSTOM_VOICE_NAME)
# gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents, 
#                           preset=preset)
# torchaudio.save(f'generated-{CUSTOM_VOICE_NAME}.wav', gen.squeeze(0).cpu(), 24000)


# custom_voice_folder = f"tortoise/voices/{CUSTOM_VOICE_NAME}"
# os.makedirs(custom_voice_folder)
# for i, file_data in enumerate(files.upload().values()):
#   with open(os.path.join(custom_voice_folder, f'{i}.wav'), 'wb') as f:
#     f.write(file_data)

# # Generate speech with the custotm voice.
# voice_samples, conditioning_latents = load_voice(CUSTOM_VOICE_NAME)
# gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents, 
#                           preset=preset)
# torchaudio.save(f'generated-{CUSTOM_VOICE_NAME}.wav', gen.squeeze(0).cpu(), 24000)

