import React from 'react';
import { AppRegistry } from 'react-native-web';
import App from '../App';

AppRegistry.registerComponent('main', () => App);
AppRegistry.runApplication('main', { rootTag: document.getElementById('root') });
