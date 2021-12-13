# Date Of Birth (and Mother's Name) )Generator

A simple Python script to consistently generate a date of birth (DoB) and a mother's name for you.

## Why?

Many websites, during signup, require that you fill in your date of birth. This is used in many cases to "prove" you're above a certain age, e.g. 13 or 18 or wahtever. In fact the DoB is not needed for that as it is no proof in itself; simply asking for your age would be enough. (IANAL but the practice is probably illegal in the EU because of GDPR; but that's a different story.) In reality this is just data harvesting.

You may need to remember your own DoB you filled in during signup in case you later want to recover your password or such. So filling in a random date is not good enough (unless you actually remember, or make your keychain remember it, or always fill in the same fake date, or ...)

As an additional feature, v0.2 also generates a semi-random "mother's name" for you, just in case.

## What?

This script generates a DoB and a "mother's name" (really just a string) for you. Given the same inputs it'll generate the same "random" DoB and name. Inputs are:
* your account name, ie. email address
* an optional service name, defaults to emppty string
* an optional minimum age (as a number, defaults to 18)

## How?

The script is really just a trivial function that takes the above arguments (at a minimum the account name) and returns a DoB and a string.

## Demo / DoB-as-a-Service

You can try this out at https://kistel.eu/dob-generator/

## Contributing

Feel free to modify as you wish, or contribute at https://github.com/robert-kisteleki/dob-generator/
