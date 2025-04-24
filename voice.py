from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

class Audio(VoiceoverScene):
    def construct(self):
        self.set_speech_service(CoquiService(transcription_model="large"))
        #CoquiService().set_transcription(model="medium")
        with self.voiceover(text="""Summary:
The coordinator from the 4th year at Heritage Institute of Technology addresses the Geeks United Students Community regarding the cancellation of the cultural fest, Eclecia, and the technical fest, Dakshh. The cancellation was due to an unfortunate incident outside the campus that could have been avoided with college authorities' intervention. Despite the challenges and limited funding, the coordinator and club coordinators worked tirelessly to organize the technical fest. However, their efforts were in vain, and the fest did not take place. The coordinator suggests that upcoming batches be cautious and raise their voices against injustices caused by the college authorities' incompetence. They hope that future students will have the opportunity to witness the Students' Council as the college returns to its normal routine."""):
            pass