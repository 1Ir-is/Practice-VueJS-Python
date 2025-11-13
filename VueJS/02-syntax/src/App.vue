<script setup>
const message = 'Hello Techzen'
const rawHtml = '<span style="color: red">This should be red.</span>'
const rawHtmlInterpolation = 'This should be red'

const buttonId = 'button-id'
const buttonClass = 'btn btn-rounded'

const isButtonDisabled = true

const objectOfAttrs = {
  id: 'container',
  class: 'wrapper',
  style: {
    color: 'blue',
    cursor: 'pointer',
    borderRadius: '50px',
    border: 'none',
    padding: '10px 17px',
  },
}

const number = 0

const listString = 'a,b,c,d,e,f,g'
const convertToId = (data) => data.split(',').reverse().join('-')

const attributeName = 'href'
const url = 'https://techzen.vn/'
</script>

<template>
  <h1>Syntax</h1>
  <p>Message: {{ message }}</p>

  <div class="demo">
    <p>
      Using text interpolation: <span style="color: red">{{ rawHtmlInterpolation }}</span>
    </p>
    <p>Using v-html directive: <span v-html="rawHtml"></span></p>
  </div>

  <button
    style="margin-bottom: 12px"
    v-bind:id="buttonId"
    :class="buttonClass"
    :disabled="isButtonDisabled"
  >
    {{ isButtonDisabled ? 'Disable' : 'Click Here' }}
  </button>

  <br />
  <button v-bind="objectOfAttrs">Click Here</button>

  <br />
  <br />

  <button :id="convertToId(listString)">Number: {{ number + 2 }}</button>
  <br />

  <a v-bind:[attributeName]="url">Click link here</a>

  <br />

  <a v-bind:href="url">Click</a>
</template>
