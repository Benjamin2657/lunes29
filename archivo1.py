import whisper
from moviepy.editor import VideoFileClip

def transcribir_video(/media/jhonatan/3743-74C1):
    video = VideoFileClip(/media/jhonatan/3743-74C1)
    audio = video.audio
    audio.write_audiofile("audio_temporal.wav")

    model = whisper.load_model("base")  
    result = model.transcribe("audio_temporal.wav")
    return result["text"]

if __name__ == "__main__":
    ruta_video = "/media/jhonatan/3743-74C1"  # Reemplaza con la ruta de tu video
    texto = transcribir_video(ruta_video)
    print(texto)
