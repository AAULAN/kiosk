import { ProductService } from './service/product.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './component/app.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ProductsOverviewComponent } from './component/products-overview/products-overview.component';
import { ProductDetailsComponent } from './component/product-details/product-details.component';

import {
  MatTableModule,
  MatButtonModule,
  MatIconModule,
  MatToolbarModule,
  MatSnackBarModule,
  MatListModule,
  MatDividerModule,
  MatDialogModule,
  MatFormFieldModule,
  MatInputModule,
  MatCheckboxModule,
  MAT_SNACK_BAR_DEFAULT_OPTIONS,
  MatTooltipModule,
  MatProgressSpinnerModule,
  MatSpinner} from '@angular/material';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { KeyInterceptor } from './interceptor/key.interceptor';

import { FlexLayoutModule } from '@angular/flex-layout';
import { FormsModule } from '@angular/forms';
import { SalesOverviewComponent } from './component/sales-overview/sales-overview.component';


@NgModule({
  declarations: [
    AppComponent,
    ProductsOverviewComponent,
    ProductDetailsComponent,
    SalesOverviewComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatTableModule,
    MatButtonModule,
    MatIconModule,
    MatToolbarModule,
    HttpClientModule,
    MatSnackBarModule,
    FlexLayoutModule,
    MatListModule,
    MatDividerModule,
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
    MatCheckboxModule,
    FormsModule,
    MatTooltipModule,
    MatProgressSpinnerModule
  ],
  providers: [{provide: MAT_SNACK_BAR_DEFAULT_OPTIONS, useValue: {duration: 1500}},
    {provide: HTTP_INTERCEPTORS, useClass: KeyInterceptor, multi: true}],
  bootstrap: [AppComponent],
  entryComponents: [ProductDetailsComponent]
})
export class AppModule { }
