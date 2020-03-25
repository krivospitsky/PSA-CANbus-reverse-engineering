// immobilizer challenge-response theorical implementation
// THIS IS NOT TESTED YET!
// This should match the authentication between the BSI and the engine ECU
// Thanks to Wouter B for the original algorithm :)

#include <inttypes.h>

// Transformation function with PSA not-so-secret sauce
int16_t transform(int16_t i, int8_t sec[])
{
	int16_t result = ((i % sec[0]) * sec[2]) - ((i / sec[0]) * sec[1]);
	if (result < 0)
		result += (sec[0] * sec[2]) + sec[1];
	return result;
}

// Challenge reponse calculation for a given pin and challenge
uint32_t compute_response(uint32_t pin, uint32_t challenge)
{
	// Hardcoded secrets...
	int8_t sec_1[3] = {0xB2, 0x3F, 0xAA};
	int8_t sec_2[3] = {0xB1, 0x02, 0xAB};

	// Compute first sub_challenge parts and sub_pin parts
	int16_t sub_ch_1 = ((challenge & 0xff000000) >> 16) | ((challenge & 0x0000ff00) >> 8);
	int16_t sub_ch_2 = ((challenge & 0x00ff0000) >> 8) | (challenge & 0x000000ff);
	int16_t sub_pin_1 = ((pin & 0xff000000) >> 16) | (pin & 0x000000ff);
	int16_t sub_pin_2 = (pin & 0x00ffff00) >> 8;

	// Compute each 16bits part of the response and return it
	int16_t res_l = transform(sub_ch_1, sec_1) | transform(sub_pin_1, sec_2);
	int16_t res_r = transform(sub_ch_2, sec_2) | transform(sub_pin_2, sec_1);
	return (res_l << 16) | res_r;
}
