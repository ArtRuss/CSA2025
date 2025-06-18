const fs = require('fs'); // NPM Filesystem package manager
const { chromium, request } = require('playwright'); // 1 dependency

const URL   = 'https://bxeregprod.oit.nd.edu/StudentRegistration/ssb/classSearch/classSearch'; // This is the "Class Search" URL.
const STATE = 'state.json'; // cookie jar


