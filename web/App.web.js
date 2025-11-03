import React from 'react';
import { View, Text, Button, StyleSheet, ScrollView } from 'react-native-web';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

// Simple screens
function HomeScreen({ navigation }) {
  const meals = [
    { id: 'm1', name: 'Oats porridge with fruits', type: 'Breakfast', calories: 320 },
    { id: 'm2', name: 'Grilled chicken salad', type: 'Lunch', calories: 420 },
    { id: 'm3', name: 'Moong dal and vegetables', type: 'Dinner', calories: 380 },
  ];

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Welcome to NutriCheck</Text>
      <Text style={styles.subtitle}>Personalized meal planning for special diets</Text>
      <View style={styles.buttonContainer}>
        <Button title="View Meal Plan" onPress={() => navigation.navigate('MealPlan')} />
        <Button title="Recommendations" onPress={() => navigation.navigate('Recommendations')} />
      </View>
      <View style={styles.mealsContainer}>
        {meals.map(meal => (
          <View key={meal.id} style={styles.card}>
            <Text style={styles.cardTitle}>{meal.name}</Text>
            <Text>{meal.calories} kcal • {meal.type}</Text>
          </View>
        ))}
      </View>
    </ScrollView>
  );
}

function MealPlanScreen() {
  const meals = [
    { id: 'm1', name: 'Oats porridge with fruits', type: 'Breakfast', calories: 320, description: 'Wholegrain oats with skim milk and seasonal fruits.' },
    { id: 'm2', name: 'Grilled chicken salad', type: 'Lunch', calories: 420, description: 'Leafy greens, grilled chicken, olive oil dressing.' },
    { id: 'm3', name: 'Moong dal and vegetables', type: 'Dinner', calories: 380, description: 'Protein-rich dal with mixed veggies and brown rice.' },
  ];

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Today's Meal Plan</Text>
      {meals.map(meal => (
        <View key={meal.id} style={styles.card}>
          <Text style={styles.cardTitle}>{meal.name}</Text>
          <Text>{meal.calories} kcal • {meal.type}</Text>
          <Text style={{ marginTop: 6 }}>{meal.description}</Text>
        </View>
      ))}
    </ScrollView>
  );
}

function RecommendationScreen() {
  const recommendations = [
    { id: 'r1', title: 'For Diabetic Patients', description: 'Prefer low glycemic-index carbs, avoid sugary drinks, replace white rice with brown rice.' },
    { id: 'r2', title: 'For Thyroid Patients', description: 'Ensure adequate iodine and selenium; avoid very high soy intake close to medication time.' },
    { id: 'r3', title: 'For B12 Deficiency', description: 'Include fortified cereals, dairy, and consider supplementation after consulting a doctor.' },
  ];

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Diet Recommendations</Text>
      {recommendations.map(rec => (
        <View key={rec.id} style={{ padding: 10, borderBottomWidth: 1, borderColor: '#eee' }}>
          <Text style={{ fontWeight: '600' }}>{rec.title}</Text>
          <Text>{rec.description}</Text>
        </View>
      ))}
    </ScrollView>
  );
}

function SettingsScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Settings</Text>
      <Text>Manage your preferences here.</Text>
    </View>
  );
}

const Stack = createStackNavigator();

function App() {
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

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, backgroundColor: '#fff' },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 8 },
  subtitle: { fontSize: 14, marginBottom: 12, color: '#444' },
  buttonContainer: { marginBottom: 20, gap: 10 },
  mealsContainer: { marginTop: 20 },
  card: { padding: 12, borderWidth: 1, borderColor: '#e5e5e5', borderRadius: 8, marginBottom: 12 },
  cardTitle: { fontWeight: '700', fontSize: 16 },
});

export default App;
