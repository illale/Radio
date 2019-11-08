/*
 * audio.c
 *
 *  Created on: 7.11.2019
 *      Author: Aleksi
 */

#include "fmod.h"
#include "fmod_common.h"
#include <stdio.h>
#include <stdlib.h>


int main() {
	FMOD_RESULT result;
	FMOD_SYSTEM *system = NULL;
	FMOD_SOUND *sound = NULL;

	result = FMOD_System_Create(&system);

	if (result != FMOD_OK) {
		printf("FMOD Error!");
		exit(-1);
	}

	result = FMOD_System_Init(system, 0, FMOD_INIT_NORMAL, NULL);

	if (result != FMOD_OK) {
		printf("FMOD Error!");
		exit(-1);
	}

	result = FMOD_System_CreateSound(system, "music.aac", FMOD_DEFAULT, NULL, &sound);

	if (result != FMOD_OK) {
		printf("FMOD Error!");
		exit(-1);
	}
	result = FMOD_System_PlaySound(system, sound, NULL, 0, NULL);

	if (result != FMOD_OK) {
		printf("FMOD Error!");
		exit(-1);
	}

	return 0;
}
