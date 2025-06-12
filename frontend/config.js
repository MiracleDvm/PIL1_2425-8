export const config = {
  googleMapsApiKey: process.env.VUE_APP_GOOGLE_MAPS_API_KEY || "YOUR_GOOGLE_MAPS_API_KEY",
  stripePublicKey: process.env.VUE_APP_STRIPE_PUBLIC_KEY || "your-stripe-public-key",
  firebaseApiKey: process.env.VUE_APP_FIREBASE_API_KEY || "your-firebase-api-key",
};
