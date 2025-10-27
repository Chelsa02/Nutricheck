
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import HomeScreen from './screens/HomeScreen';
import MealPlanScreen from './screens/MealPlanScreen';
import RecommendationScreen from './screens/RecommendationScreen';
import SettingsScreen from './screens/SettingsScreen';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="MealPlan" component={MealPlanScreen} options={{ title: 'Meal Plan' }} />
        <Stack.Screen name="Recommendations" component={RecommendationScreen} options={{ title: 'Diet Recommendations' }} />
        <Stack.Screen name="Settings" component={SettingsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
