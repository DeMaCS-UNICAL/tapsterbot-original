/*
    MIT License
    Copyright (c) 2018 Pierre-Yves Lapersonne (Mail: dev@pylapersonne.info)
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
 */
// ✿✿✿✿ ʕ •ᴥ•ʔ/ ︻デ═一

package pylapp.tapster.client.android.vox

import android.content.Context

/**
 * Stub based on design pattern Bridge which provides the declarations of methods to call
 * so as to deal with TTS features.
 * This pattern is used so as to avoid an activity or something else to have too many dependencies
 * and code about the way TTS is made.
 * A library may be used, so let's thing a step further in case of the death of this library.
 *
 * @author Pierre-Yves Lapersonne
 * @since 08/02/2018
 *
 * @version 1.0.0
 */
interface TextToSpeechStub {

    /**
     * Initializes the TTS system
     *
     * @param context - The context to use to initialize the system
     */
    fun init(context: Context)

    /**
     * Vocalizes the text
     *
     * @param text - The vocalized texts
     */
    fun speak(text: String)

    /**
     * Stops the vocalization
     */
    fun stop()

    /**
     * Frees the resources, stops listeners and clean all the things.
     * The TTS system will be then destroyed.
     */
    fun shutdown()

}